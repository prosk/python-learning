def get_desc():
    first_name = "ada"
    second_name = "Lovelace"
    desc = "PROGRAMMER"
    first_name = first_name.title()
    second_name = second_name.upper()
    desc = desc.lower()
    text = f"{first_name} - {second_name}: {desc}"
    return text

def main():
    desc = get_desc()
    print(desc)


if __name__ == "__main__":
    main()