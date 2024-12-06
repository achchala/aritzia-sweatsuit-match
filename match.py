import requests
from bs4 import BeautifulSoup

# product URLs
sweats_urls = [
    "https://www.aritzia.com/en/product/cozy-fleece-mega-cargo%E2%84%A2-sweatpant/116229020.html",
    "https://www.aritzia.com/en/product/cozy-fleece-mega-straight%E2%84%A2-sweatpant/119382023.html",
]
hoodies_urls = [
    "https://www.aritzia.com/product/https://www.aritzia.com/en/product/cozy-fleece-mega-raglan%E2%84%A2-hoodie/116266092.html",
    "https://www.aritzia.com/en/product/cozy-fleece-perfect-hoodie/116209078.html",
]

# sizes looking for
desired_sizes_pants = ["S"]
desired_sizes_hoodie = ["S", "M"]


# function to check size availability
def check_availability(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # parsing available sizes (need to adjust selectors based on Aritzia's HTML)
    color_elements = soup.select(
        ".color-name"
    )  # Replace with actual selector for color
    size_elements = soup.select(
        ".size-option"
    )  # Replace with actual selector for sizes

    colors = [color.get_text(strip=True) for color in color_elements]
    sizes = [
        size.get_text(strip=True)
        for size in size_elements
        if "available" in size["class"]
    ]

    return colors, sizes


# function to find matching items
def find_matches(sweats, hoodies):
    matches = []
    for sweat_color, sweat_sizes in sweats.items():
        for hoodie_color, hoodie_sizes in hoodies.items():
            if sweat_color == hoodie_color:
                matched_sizes = (
                    set(sweat_sizes) & set(hoodie_sizes) & set(desired_sizes)
                )
                if matched_sizes:
                    matches.append((sweat_color, matched_sizes))
    return matches


# main script
def main():
    sweats_data = {}
    hoodies_data = {}

    # check availability for sweats
    for url in sweats_urls:
        colors, sizes = check_availability(url)
        for color in colors:
            sweats_data[color] = sizes

    # check availability for hoodies
    for url in hoodies_urls:
        colors, sizes = check_availability(url)
        for color in colors:
            hoodies_data[color] = sizes

    # find matches
    matches = find_matches(sweats_data, hoodies_data)

    if matches:
        print("Matching items found:")
        for color, sizes in matches:
            print(f"Color: {color}, Sizes: {', '.join(sizes)}")
    else:
        print("No matching items found.")


if __name__ == "__main__":
    main()
