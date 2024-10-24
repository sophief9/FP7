def mad_libs():
    print("Welcome to the Mad Libs game!")
    print("Please provide the following words:")

    # Collecting inputs from the user
    large_object = input("A large object: ")
    large_objects_plural = input("Large objects (plural): ")
    adjective = input("An adjective: ")
    body_part = input("A body part: ")
    restaurant = input("A restaurant: ")
    food1 = input("A food: ")
    food2 = input("Another food: ")

    # The story template
    story = (
        f"I’ve had a very {adjective} day.\n"
        f"This morning, I dropped a box of {large_objects_plural} on my {body_part}.\n"
        f"Then, at lunch, I went to {restaurant} for their delicious {food1},\n"
        f"But the waiter brought me {food2}, which I was not hungry for.\n"
        f"Finally, on my way home, I was cut off by a van with a large {large_object} strapped to the roof."
    )

    # Display the completed story
    print("\nHere’s your Mad Lib story:\n")
    print(story)

# Run the Mad Libs game
mad_libs()
