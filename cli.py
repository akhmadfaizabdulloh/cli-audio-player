#!/usr/bin/env python3

from utils import check_dependencies
from search import search
from player import play

def main():
    check_dependencies()
    print("✅ Semua dependency tersedia")
    print("CLI Audio Player 🎧 already used")

    query = input("Search: ").strip()
    if not query:
        print("❌ Search tidak boleh kosong")
        return
    
    print("🔍 Mencari...")
    results = search(query)

    if not results:
        print("❌ Tidak ada hasil")
        return
    
    print("\nHasil:")
    for i, item in enumerate(results, start=1):
        print(f"{i}. {item['title']}")

    choice = input("\nPilih nomor (q untuk keluar): ").strip()

    if choice.lower() == "q":
        return

    if not choice.isdigit():
        print("❌ Input tidak valid")
        return
    
    index = int(choice) - 1
    if index < 0 or index >= len(results):
        print("❌ Nomor diluar range")
        return
    
    play(results[index]["url"])

if __name__ == "__main__":
    main()