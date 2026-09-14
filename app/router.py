from semantic_router import Route
from semantic_router.routers import SemanticRouter
from semantic_router.encoders import HuggingFaceEncoder

encoder = HuggingFaceEncoder(
    name="sentence-transformers/all-MiniLM-L6-v2"
)

faq = Route(
    name='faq',
    utterances=[
        "What is the return policy?",
        "Do I get discount with the HDFC credit card?",
        "How can I track my order?",
        "What payment methods are accepted?",
        "How long does it take to process a refund?",
        "What is your warranty or replacement policy?",
        "What is your policy on defective items?",
    ],
    score_threshold=0.2
)

sql = Route(
    name='sql',
    utterances=[
        "I want to buy nike shoes that have 50% discount.",
        "Are there any shoes under Rs. 3000?",
        "Do you have formal shoes in size 9?",
        "Are there any Puma shoes on sale?",
        "What is the price of puma running shoes?",
        "give me top rated products having rating more than 4.0",
        "list here all products which you have",
        "show me all products",
        "show top rated products",
        "what products do you have?",
        "list available products",
        "find products with rating greater than 4",
        "show products on discount",
        "recommend top products",
    ],
    score_threshold=0.2
)

small_talk = Route(
    name='small_talk',
    utterances=[
        "How are you?",
        "What is your name?",
        "Are you a robot?",
        "What are you?",
        "What do you do?",
    ],
    score_threshold=0.2
)

router = SemanticRouter(routes=[faq, sql, small_talk], encoder=encoder, auto_sync="local")

if __name__ == "__main__":
    print(router("What is your policy on defective product?").name)
    print(router("Pink Puma shoes in price range 5000 to 1000").name)