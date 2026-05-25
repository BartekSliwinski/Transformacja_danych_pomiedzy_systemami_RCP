# Założenia projektu

Firma planuje migrację do nowego systemu Rejestracji Czasu Pracy pracowników.
Aby zapewnić płynne i bezproblemowe przejście, zdecydowano o stopniowym wdrażaniu nowego rozwiązania, co oznacza, że przez pewien czas oba systemy będą funkcjonować równolegle.

W związku z tym konieczne jest przygotowanie rozwiązania umożliwiającego automatyczną synchronizację danych pomiędzy dotychczasowym a nowym systemem.
Pozwoli to zachować spójność informacji w obu środowiskach oraz zapewni szybkie i bezpieczne przejście po całkowitym wyłączeniu starego rozwiązania.

# Założenia techniczne
* Stary system przechowuje dane w bazie danych znajdującej się na lokalnym serwerze.
* Nowy system korzysta z bazy danych hostowanej w chmurze.
* W obu systemach przechowywane dane różnią się znacząco. Wymagana będzie ich transormacja.
* Synchronizacja danych powinna odbywać się automatycznie w określonych odstępach czasu.
* Dane muszą być przesyłane w sposób zapewniający spójność i integralność.
* Rozwiązanie powinno umożliwiać monitorowanie procesu synchronizacji oraz obsługę błędów.
* System powinien być przygotowany na przyszłe wyłączenie starego źródła danych bez konieczności zmian po stronie nowego systemu.
