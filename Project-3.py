# Catalog: each item has a name and a set of descriptive tags 
CATALOG = [
    {"name": "Inception",            "type": "Movie", "tags": {"sci-fi", "thriller", "mind-bending", "action"}},
    {"name": "The Office",           "type": "TV Show", "tags": {"comedy", "workplace", "sitcom"}},
    {"name": "Interstellar",         "type": "Movie", "tags": {"sci-fi", "space", "drama", "emotional"}},
    {"name": "Stranger Things",      "type": "TV Show", "tags": {"sci-fi", "horror", "mystery", "friendship"}},
    {"name": "The Alchemist",        "type": "Book", "tags": {"adventure", "philosophy", "inspiring"}},
    {"name": "Sapiens",              "type": "Book", "tags": {"history", "science", "non-fiction"}},
    {"name": "Breaking Bad",         "type": "TV Show", "tags": {"crime", "thriller", "drama", "intense"}},
    {"name": "Friends",              "type": "TV Show", "tags": {"comedy", "sitcom", "friendship"}},
    {"name": "The Martian",          "type": "Movie", "tags": {"sci-fi", "space", "survival", "science"}},
    {"name": "Atomic Habits",        "type": "Book", "tags": {"self-help", "psychology", "non-fiction"}},
    {"name": "Parasite",             "type": "Movie", "tags": {"thriller", "drama", "social", "intense"}},
    {"name": "Cosmos",               "type": "TV Show", "tags": {"science", "space", "documentary"}},
]

def get_user_interests():
# Ask the user for interests and return them as a clean set of tags.
    print("Tell me some things you're interested in (comma-separated).")
    print("Examples: sci-fi, comedy, space, history, thriller, self-help...\n")
    raw = input("Your interests: ")
    interests = {word.strip().lower() for word in raw.split(",") if word.strip()}
    return interests

def score_item(item, interests):
# Return how many of the user's interests overlap with an item's tags.
    return len(item["tags"] & interests)

def recommend(interests, catalog=CATALOG, top_n=5):
# Return the top_n catalog items ranked by overlap with user interests.
    scored = [(item, score_item(item, interests)) for item in catalog]
    # Keep only items with at least one matching tag
    matched = [pair for pair in scored if pair[1] > 0]
    # Sort by score, highest first
    matched.sort(key=lambda pair: pair[1], reverse=True)
    return matched[:top_n]

def display_recommendations(matched):
    if not matched:
        print("\nNo close matches found. Try different or broader interests!")
        return

    print("\nHere's what I'd recommend for you:\n")
    for rank, (item, score) in enumerate(matched, start=1):
        matched_tags = ", ".join(sorted(item["tags"]))
        print(f"{rank}. {item['name']} ({item['type']}) — match score: {score}")
        print(f"   tags: {matched_tags}\n")


print("=== Simple Recommendation System ===\n")
interests = get_user_interests()

if not interests:
    print("You didn't enter any interests, so I can't make recommendations.")
    
results = recommend(interests)
display_recommendations(results)