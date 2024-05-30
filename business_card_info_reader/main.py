from business_card_info_reader.models import OpenAIModel


def main():
    business_cards = [
        "https://marketplace.canva.com/EAE9DLlt6dY/1/0/1600w/canva-white-blue-modern-real-estate-agent-business-card-6RI4Bfnub1M.jpg",
        "https://img.freepik.com/free-vector/modern-black-white-business-card-design_1017-14939.jpg?w=1380&t=st=1716968119~exp=1716968719~hmac=ff1d76f73142fe59b8e6eb273beeb6803b1e402ab68c07c38febbdddfd526b27",
    ]
    image_url = business_cards[0]  # Change this to test with different images
    model = OpenAIModel()
    response = model.analyze_image(image_url)
    print(response)  # For demonstration, directly print the response


if __name__ == "__main__":
    main()
