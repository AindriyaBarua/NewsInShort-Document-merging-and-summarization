import utils
from nltk.corpus import stopwords


choice = 'y'
hin_occured = False
en_occured = False
lang_code_hin = "hi"
lang_code_en = "en"
ft_hin = None
ft_en = None

def chooseLangVariables(language):
    global hin_occured
    global en_occured
    print("Please wait till we set up the app for you!")
    if "hindi" == language or "english" == language:
        if "hindi" == language:
            language_code = lang_code_hin
            embedding_model_name = 'cc.' + language_code + '.300.bin'
            if not hin_occured:
                hin_occured = True
                ft_hin = utils.loadEmbeddingModel(language_code, embedding_model_name)
                hin_stopwords = utils.getHindiStopwords()
            ft_model = ft_hin
            stopwords_list = hin_stopwords

        else:
            if "english" == language:
                language_code = lang_code_en
                embedding_model_name = 'cc.' + language_code + '.300.bin'
                if not en_occured:
                    en_occured = True
                    embedding_model_name = 'cc.' + language_code + '.300.bin'
                    ft_en = utils.loadEmbeddingModel(language_code, embedding_model_name)
                    en_stopwords = stopwords.words("english")
            ft_model = ft_en
            stopwords_list = en_stopwords

        print("Set up complete!")
        return language_code, embedding_model_name, embedding_model_name, ft_model, stopwords_list
    else:
        print("Wrong choice of language. Please try again with Hindi or English.")
        exit()


if __name__=="__main__":
    print("Welcome to NewsNow!")

    while choice.lower() == 'y':
        language_prev = None
        language = input("Enter language of query. We support Hindi and English at present: ").lower()
        language_code, embedding_model_name, embedding_model_name, ft_model, stopwords_list = chooseLangVariables(language)

        query = input("Enter query to search: ").lower()

        links = utils.getLinks(query, 5)
        articles = utils.getDocuments(links)
        merged_article = utils.merge(articles, ft_model)
        summary = utils.summarize(merged_article, stopwords_list)
        print(f"Latest on {query}:\n{summary}\n")
        choice = input("Search for another article? [y/n]: ")
