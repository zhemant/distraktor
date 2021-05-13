import yaml

def main():
	config = yaml.load(open("./config.yml"), Loader=yaml.BaseLoader))

if __name__ == "__main__":
    main()
