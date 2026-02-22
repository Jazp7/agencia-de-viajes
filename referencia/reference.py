import sqlite3

class Vuelo:
    def __init__(self, id_vuelo, destino, capacidad, ocupados):
        self.id = id_vuelo
        self.destino = destino
        self.capacidad = capacidad
        self.ocupados = ocupados
        # Calculamos los asientos libres restando los ocupados
        self.disponibles = capacidad - ocupados

    def __str__(self):
        return f"ID: {self.id} | Destino: {self.destino} | Libres: {self.disponibles}/{self.capacidad}"

class Pasajero:
    def __init__(self, nombre):
        self.nombre = nombre

class Agencia:
    def __init__(self):
        self.conn = sqlite3.connect(":memory:") 
        self.cursor = self.conn.cursor()
        self._preparar_db()

    def _preparar_db(self):
        self.cursor.execute("CREATE TABLE vuelos (id INTEGER PRIMARY KEY, destino TEXT, capacidad INTEGER)")
        self.cursor.execute("CREATE TABLE reservas (id_vuelo INTEGER, nombre_pasajero TEXT)")
        self.cursor.executemany("INSERT INTO vuelos VALUES (?, ?, ?)", [
            (1, "Madrid", 2), 
            (2, "San Salvador", 10),
            (3, "Tokyo", 1)
        ])
        self.conn.commit()

    def obtener_vuelos_disponibles(self):
        """
        Esta consulta SQL es la clave: 
        Cuenta cuántas reservas tiene cada vuelo y solo trae los que tienen cupo.
        """
        query = """
            SELECT v.id, v.destino, v.capacidad, COUNT(r.id_vuelo) as ocupados
            FROM vuelos v
            LEFT JOIN reservas r ON v.id = r.id_vuelo
            GROUP BY v.id
            HAVING ocupados < v.capacidad
        """
        self.cursor.execute(query)
        filas = self.cursor.fetchall()
        # Creamos objetos Vuelo con la información procesada
        return [Vuelo(f[0], f[1], f[2], f[3]) for f in filas]

    def reservar_vuelo(self, id_vuelo, pasajero):
        # La lógica de reserva se mantiene similar, pero ahora recibe un OBJETO Pasajero
        self.cursor.execute("SELECT capacidad FROM vuelos WHERE id = ?", (id_vuelo,))
        resultado = self.cursor.fetchone()
        
        if not resultado:
            print("❌ El vuelo no existe.")
            return

        capacidad = resultado[0]
        self.cursor.execute("SELECT COUNT(*) FROM reservas WHERE id_vuelo = ?", (id_vuelo,))
        ocupados = self.cursor.fetchone()[0]

        if ocupados < capacidad:
            # Usamos el atributo .nombre del objeto pasajero
            self.cursor.execute("INSERT INTO reservas VALUES (?, ?)", (id_vuelo, pasajero.nombre))
            self.conn.commit()
            print(f"✅ ¡Reserva exitosa para {pasajero.nombre}!")
        else:
            print("❌ Error: Ya no hay cupos para este destino.")

# --- INTERFAZ ---
def ejecucion():
    agencia = Agencia()
    # Creamos una instancia de Pasajero con el nombre del usuario
    usuario = Pasajero(input("Bienvenido, ¿cómo te llamas?: "))

    while True:
        print(f"\n--- SESIÓN: {usuario.nombre} ---")
        print("1. Ver vuelos con cupo")
        print("2. Reservar un vuelo")
        print("3. Salir")
        op = input("Selecciona: ")

        if op == "1":
            vuelos = agencia.obtener_vuelos_disponibles()
            if not vuelos:
                print("No hay vuelos disponibles en este momento.")
            for v in vuelos:
                print(v) 

        elif op == "2":
            id_v = int(input("ID del vuelo: "))
            agencia.reservar_vuelo(id_v, usuario) # Pasamos el objeto completo

        elif op == "3":
            break

if __name__ == "__main__":
    ejecucion()