class CSVBaseRepository:
    def __init__(self, file_path):
        """
        Luokan konstruktori.

        Args:
            file_path: Polku CSV-tiedostoon, johon tapahtumat tallennetaan.
        """
        self._file_path = file_path

    def _read_csv_file(self):
        rows = []
        with open(self._file_path, encoding="utf-8") as file:
            for row in file:
                row = row.replace("\n", "")
                parts = row.split(";")
                rows.append(parts)
        return rows
