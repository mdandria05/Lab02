from csv import writer

class Libro:
    def __init__(self):
        self.titolo = ""
        self.autore = ""
        self.data = ""
        self.pagine = -1
        self.n_sezione = -1

    def in_titolo(self,titolo):
        self.titolo = titolo
    def in_autore(self,autore):
        self.autore = autore
    def in_data(self,data):
        self.data = data
    def in_pagine(self,pagine):
        self.pagine = pagine
    def in_n_sezione(self,n_sezione):
        self.n_sezione = n_sezione

    def out_titolo(self):
        return self.titolo
    def out_autore(self):
        return self.autore
    def out_data(self):
        return self.data
    def out_pagine(self):
        return str(self.pagine)
    def out_n_sezione(self):
        return str(self.n_sezione)

    def check_title(self,titolo):
        if titolo.lower() == self.titolo.lower():
            return True
        else: return False

    def check_sezione(self,n_sezione):
        if n_sezione ==self.n_sezione:
            return True
        else: return False

def carica_da_file(file_path):
    """Carica i libri dal file"""
    # TODO
    try:
        infile = open(file_path, "r", encoding="utf-8")
    except FileNotFoundError:
        print("File not found...\n")
        return None
    biblioteca = []
    max_sezioni = infile.readline()
    for line in infile:
        l = Libro()
        words = line.split(",")
        try:
            l.in_titolo(words[0].rstrip(""))
            l.in_autore(words[1].rstrip(""))
            l.in_data(str(words[2].rstrip("")))
            l.in_pagine(int(words[3].rstrip("")))
            l.in_n_sezione(int(words[4].rstrip("\n")))
            biblioteca.append(l)
        except IndexError as e:
            continue
    return list(biblioteca)

def aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path):
    """Aggiunge un libro nella biblioteca"""
    # TODO
    for l in biblioteca:
        if l.check_title(titolo): return None
    else:
        infile = open(file_path, "a", encoding="utf-8")
        csvWriter = writer(infile)
        csvWriter.writerow([titolo,autore,anno,int(pagine),int(sezione)])
        l = Libro()
        titolo = titolo[0].upper()+titolo[1:]
        l.in_titolo(titolo)
        l.in_autore(autore)
        l.in_data(anno)
        l.in_pagine(pagine)
        l.in_n_sezione(sezione)
        biblioteca.append(l)

def cerca_libro(biblioteca, titolo):
    """Cerca un libro nella biblioteca dato il titolo"""
    # TODO
    check = False
    for l in biblioteca:
        if not check:
            if l.check_title(titolo):
                libro = l.out_titolo(),l.out_autore(),l.out_data(),l.out_pagine(),l.out_n_sezione()
                return libro
        else:
            return None



def elenco_libri_sezione_per_titolo(biblioteca, sezione):
    """Ordina i titoli di una data sezione della biblioteca in ordine alfabetico"""
    # TODO
    l_ordinati = []
    for l in biblioteca:
        if l.check_sezione(sezione):
            l_ordinati.append(l.out_titolo())
    l_ordinati.sort()
    return list(l_ordinati)


def main():
    biblioteca = []
    file_path = "biblioteca.csv"

    while True:
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Carica biblioteca da file")
        print("2. Aggiungi un nuovo libro")
        print("3. Cerca un libro per titolo")
        print("4. Ordina titoli di una sezione")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                biblioteca = carica_da_file(file_path)
                if biblioteca is not None:
                    break

        elif scelta == "2":
            if not biblioteca:
                print("Prima carica la biblioteca da file.")
                continue

            titolo = input("Titolo del libro: ").strip()
            autore = input("Autore: ").strip()
            try:
                anno = int(input("Anno di pubblicazione: ").strip())
                pagine = int(input("Numero di pagine: ").strip())
                sezione = int(input("Sezione: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per anno, pagine e sezione.")
                continue

            libro = aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path)
            if libro:
                print(f"Libro aggiunto con successo!")
            else:
                print("Non è stato possibile aggiungere il libro.")

        elif scelta == "3":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            titolo = input("Inserisci il titolo del libro da cercare: ").strip()
            risultato = cerca_libro(biblioteca, titolo)
            if risultato:
                print(f"Libro trovato: {risultato}")
            else:
                print("Libro non trovato.")

        elif scelta == "4":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            try:
                sezione = int(input("Inserisci numero della sezione da ordinare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_libri_sezione_per_titolo(biblioteca, sezione)
            if titoli is not None:
                print(f'\nSezione {sezione} ordinata:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")

if __name__ == "__main__":
    main()

