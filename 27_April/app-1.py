import config

def main():
    # Load configuration
    settings = config.Config.get_config()

    print("Application Configuration:")
    for key, value in settings.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
