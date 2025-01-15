from langchain_gigachat.chat_models import GigaChat
from langchain_core.output_parsers import StrOutputParser

from langchain_core.prompts import ChatPromptTemplate


def get_gigachat_answer(id: str, news: str, instruction: str) -> str:

    model = GigaChat(
        credentials=id,
        scope="GIGACHAT_API_PERS",
        model="GigaChat",
        verify_ssl_certs=False,
    )
    parser = StrOutputParser()

    prompt_translate = ChatPromptTemplate.from_messages([
        ("system", "Переведи следующий текст на русский. Не переводи имена \
         собственные и названия команд. Текст для перевода:"),
        ("user", "{text}")
    ])

    prompt_digest = ChatPromptTemplate.from_messages([
        ("system", instruction),
        ("user", "{text}")
    ])

    chain_translate = prompt_translate | model | parser
    translated_news = chain_translate.invoke({"text": news})

    chain_digest = prompt_digest | model | parser
    result = chain_digest.invoke({"text": translated_news})

    return result


# def get_kandinsky_img(digest: str):

#     model = GigaChat(
#         credentials=id,
#         scope="GIGACHAT_API_PERS",
#         model="GigaChat",
#         verify_ssl_certs=False,
#     )
#     parser = StrOutputParser()

#     prompt_for_prompt = ChatPromptTemplate.from_messages([
#         ("system", "Прочитай дайджест событиый в НБА и \
#          выбери один наиболее яркий инфоповод для генерации картинки. \
#          В ответ напиши мне промпт для генерации изображения в kandinski \
#          на основе. Текст дайджеста: "),
#         ("user", "{text}")
#     ])

#     chain_translate = prompt_for_prompt | model | parser
#     kandinsky_prompt = chain_translate.invoke({"text": digest})

#     return kandinsky_prompt
