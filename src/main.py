from load_data import load_data
from clean_data import clean_data
from analysis import analyze_data
from visualization import create_charts

def main():
    df = load_data()
    df = clean_data(df)

    results = analyze_data(df)

    for key, value in results.items():
        print(f"\n{key.upper()}:\n", value)

if __name__ == "__main__":
    main()

    df = load_data()
    df = clean_data(df)

    results = analyze_data(df)

    create_charts(df)

    for key, value in results.items():
        print(f"\n{key.upper()}:\n", value)