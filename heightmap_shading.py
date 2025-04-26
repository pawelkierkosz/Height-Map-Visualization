import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import hsv_to_rgb

def wczytaj_dane(plik):
    # Wczytuje dane z pliku i zwracam wymiary oraz tablicę danych
    with open(plik, "r") as f:
        linie = f.readlines()

    szerokosc, wysokosc, odleglosc = map(int, linie[0].split())
    dane = np.array([linia.split() for linia in linie[1:]], dtype='float')

    return szerokosc, wysokosc, odleglosc, dane

def hsv_do_rgb(h, s, v):
    # Konwertuje kolor z przestrzeni HSV do RGB
    return hsv_to_rgb([h, s, v])

def mapa_kolorow(v, intensywnosc, maks_wartosc, min_wartosc):
    # Mapuje wartość wysokości i intensywność na kolor RGB
    h = (maks_wartosc - v) * 120 / (maks_wartosc - min_wartosc)
    s = 1
    return hsv_do_rgb(h / 360, s, intensywnosc)

def oblicz_normalna(dane, i, j, odleglosc):
    # Obliczam wektor normalny dla punktu (i, j)
    if i > 0 and i < dane.shape[0] - 1 and j > 0 and j < dane.shape[1] - 1:
        dzdx = (dane[i+1, j] - dane[i-1, j]) / (2 * odleglosc)
        dzdy = (dane[i, j+1] - dane[i, j-1]) / (2 * odleglosc)
        normalna = np.array([-dzdx, -dzdy, 1.0])
        return normalna / np.linalg.norm(normalna)
    return np.array([0, 0, 1])  # Domyślny wektor normalny dla krawędzi

def rysuj_mape_wysokosci_proste_cieniowanie(dane, szerokosc, wysokosc, maks_wartosc, min_wartosc):
    # Tworze obraz z prostym cieniowaniem
    obraz = np.zeros((szerokosc, wysokosc, 3))

    for i in range(szerokosc):
        for j in range(wysokosc):
            if j > 0:
                if dane[i, j] > dane[i, j - 1]:
                    intensywnosc = 0.7  # Przyciemnij
                else:
                    intensywnosc = 1.0  # Rozjaśnij
            else:
                intensywnosc = 1.0  # Brak lewego sąsiada
            obraz[i, j] = mapa_kolorow(dane[i, j], intensywnosc, maks_wartosc, min_wartosc)

    # Wyświetlam mapę z prostym cieniowaniem
    plt.figure(figsize=(10, 10))
    plt.title("Proste cieniowanie")
    plt.imshow(obraz)
    plt.show()

def rysuj_mape_wysokosci_zaawansowane_cieniowanie(dane, szerokosc, wysokosc, maks_wartosc, min_wartosc):
    # Tworze obraz z zaawansowanym cieniowaniem
    kierunek_swiatla = np.array([1, 1, 0.5])  # Zródło światła znajduje się w lewym górnym rogu
    kierunek_swiatla = kierunek_swiatla / np.linalg.norm(kierunek_swiatla)

    obraz = np.zeros((szerokosc, wysokosc, 3))

    for i in range(szerokosc):
        for j in range(wysokosc):
            normalna = oblicz_normalna(dane, i, j, 1)
            iloczyn_skalarny = np.dot(normalna, kierunek_swiatla)
            intensywnosc = 0.5 + 0.5 * max(0, iloczyn_skalarny)  # Obliczam intensywność oświetlenia
            obraz[i, j] = mapa_kolorow(dane[i, j], intensywnosc, maks_wartosc, min_wartosc)

    # Wyświetla mapę z zaawansowanym cieniowaniem
    plt.figure(figsize=(10, 10))
    plt.title("Zaawansowane cieniowanie")
    plt.imshow(obraz)
    plt.show()

# Wczytuje dane z pliku
szerokosc, wysokosc, odleglosc, dane = wczytaj_dane("big.dem")

# Oblicza wartości maksymalne i minimalne
maks_wartosc = np.amax(dane)
min_wartosc = np.amin(dane)

# Rysuje mapę wysokości z prostym cieniowaniem
rysuj_mape_wysokosci_proste_cieniowanie(dane, szerokosc, wysokosc, maks_wartosc, min_wartosc)

# Rysuje mapę wysokości z zaawansowanym cieniowaniem
rysuj_mape_wysokosci_zaawansowane_cieniowanie(dane, szerokosc, wysokosc, maks_wartosc, min_wartosc)
