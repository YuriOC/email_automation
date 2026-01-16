import os
import io
import spacy

from pypdf import PdfReader
from flask import json
from dotenv import load_dotenv
from openai import OpenAI

lemmatize_load = spacy.load("pt_core_news_sm")

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

class EmptyFileError(Exception):
    pass

class FileReadError(Exception):
    pass    

def pdfReader(file):
    try:
        pdf_reader = PdfReader(io.BytesIO(file.read()))
        content = ""
        for page in pdf_reader.pages:
            txt = page.extract_text()
            if txt:
                content += txt + "\n"
        return content.strip()
    except Exception as e:
        return f"Error reading PDF: {str(e)}", 500
    
def read_file(file, filename):
    try:
        if filename.endswith('.txt'):
            content = file.read().decode('utf-8')
        elif filename.endswith('.pdf'):
            content = pdfReader(file)
        else:
            raise ValueError("Unsupported file format. Please upload a .txt or .pdf file.")
        
        if not content or not content.strip():
            raise EmptyFileError("The uploaded file is empty.")
        
        return content
    
    except EmptyFileError:
        raise

    except Exception as e:
        raise FileReadError(f"Error reading file: {filename}") from e

def lemmatize_text(full_text: str) -> list[str]:
    
    doc = lemmatize_load(full_text.lower())

    lemmas = [
        token.lemma_
        for token in doc
        if not token.is_stop
        and not token.is_punct
        and not token.is_space
        and token.is_alpha
    ]

    return lemmas


def email_classification_AI(full_text: str):

    lemmatized_list = lemmatize_text(full_text)
    lemmatized_text = " ".join(lemmatized_list)

    try:
        response = client.chat.completions.create(
            model="gpt-5-nano",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Você é um assistente corporativo especializado em triagem e resposta automática de emails.\n\n"

                        "### OBJETIVO\n"
                        "1. Classificar o email como PRODUTIVO ou IMPRODUTIVO.\n"
                        "2. Gerar uma resposta profissional e adequada à classificação.\n\n"

                        "### DEFINIÇÕES\n"
                        "- PRODUTIVO: requer ação ou acompanhamento humano "
                        "(suporte, erros, dúvidas, cobranças, solicitações, atualizações).\n"
                        "- IMPRODUTIVO: não requer ação imediata "
                        "(agradecimentos, felicitações, mensagens informativas).\n\n"

                        "### REGRAS OBRIGATÓRIAS\n"
                        "- Use o TEXTO LEMATIZADO APENAS para CLASSIFICAÇÃO.\n"
                        "- Use o TEXTO ORIGINAL APENAS para REDIGIR A RESPOSTA.\n"
                        "- NÃO utilize palavras lematizadas na resposta.\n"
                        "- NÃO invente informações.\n"
                        "- Se faltar contexto, solicite esclarecimentos educadamente.\n\n"

                        "### TOM DE VOZ\n"
                        "- PRODUTIVO: profissional, solícito e proativo.\n"
                        "- IMPRODUTIVO: cordial, breve e educado.\n\n"

                        "### FORMATO DE SAÍDA (OBRIGATÓRIO)\n"
                        "Retorne APENAS um JSON válido no formato:\n"
                        "{\n"
                        "  \"classificacao\": \"PRODUTIVO | IMPRODUTIVO\",\n"
                        "  \"resposta_sugerida\": \"texto da resposta\"\n"
                        "}"
                    )
                },

                {
                    "role": "user",
                    "content": (
                        "### CLASSIFICAÇÃO (use APENAS o texto abaixo)\n"
                        f"{lemmatized_text}"
                    )
                },

                {
                    "role": "user",
                    "content": (
                        "### RESPOSTA (use APENAS o texto abaixo)\n"
                        f"{full_text}"
                    )
                }
            ],
            response_format={"type": "json_object"}
        )

        resultado = json.loads(response.choices[0].message.content)

        if (
            "classificacao" not in resultado
            or "resposta_sugerida" not in resultado
        ):
            raise ValueError("Formato de resposta inválido")

        return resultado

    except Exception as e:
        return {
            "classificacao": "ERRO",
            "resposta_sugerida": (
                "Agradecemos o contato. "
                "No momento, não foi possível processar sua mensagem automaticamente. "
                "Nossa equipe fará a análise em breve."
            )
        }, 500, {"error": str(e)}