from apps.model_provider_mgmt.models import EmbedModelChoices
from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings import FastEmbedEmbeddings


class EmebdDriver:
    def get_embedding(self, embed_model):
        model_configs = embed_model.embed_config
        if embed_model.embed_model == EmbedModelChoices.FASTEMBED:
            embedding = FastEmbedEmbeddings(model_name=model_configs['model'], cache_dir='models')
        if embed_model.embed_model == EmbedModelChoices.OPENAI:
            embedding = OpenAIEmbeddings(model=model_configs['model'],
                                         openai_api_key=model_configs['openai_api_key'],
                                         openai_api_base=model_configs['openai_base_url'])
        return embedding
