from __future__ import annotations

from pathlib import Path
import struct


class BinaryReader:

    def __init__(self, path: str | Path) -> None:
        self.path = path

    def __enter__(self) -> BinaryReader:
        self.stream = open(self.path, "rb")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.stream.close()
        return exc_type is None

    def __read_bytes(self, format: str, size_en_octets: int):

        donnees_binaires = self.stream.read(size_en_octets)

        if not donnees_binaires:
            raise EOFError()

        return struct.unpack(format, donnees_binaires)[0]

    def read_float32(self) -> float:
        return self.__read_bytes("<f", 4)

    def read_float64(self) -> float:
        return self.__read_bytes("<d", 8)

    def read_byte(self) -> int:
        return self.__read_bytes("<B", 1)

    def read_bytes(self, size: int) -> bytes:
        donnees_binaires = self.stream.read(size)
        if not donnees_binaires:
            raise EOFError()
        return donnees_binaires

    def read_bool(self) -> bool:
        return bool(self.__read_bytes("<B", 1))

    def read_int32(self) -> int:
        return self.__read_bytes("<i", 4)

    def read_int64(self) -> int:
        return self.__read_bytes("<q", 8)


class BinaryWriter:

    def __init__(self, nom_fichier):
        self.nom_fichier = nom_fichier

    def __enter__(self):
        self.stream = open(self.nom_fichier, "wb")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):

        if self.stream:
            self.stream.close()

        return exc_type is None

    def __write_bytes(self, format: str, value):
        packed_data = struct.pack(format, value)
        self.stream.write(packed_data)

    def write_float32(self, value: float):
        self.__write_bytes("<f", value)

    def write_float64(self, value: float):
        self.__write_bytes("<d", value)

    def write_byte(self, value: int):
        self.__write_bytes("<B", value)

    def write_bytes(self, data: bytes):
        self.stream.write(data)

    def write_bool(self, value: bool):
        self.__write_bytes("<B", 1 if value else 0)

    def write_int32(self, value: int):
        self.__write_bytes("<i", value)

    def write_int64(self, value: int):
        self.__write_bytes("<q", value)


if __name__ == "__main__":

    with BinaryWriter("file.bin") as writer:
        writer.write_float64(3.14159)
        writer.write_int32(12345)
        writer.write_byte(255)
        writer.write_bool(True)
        writer.write_float64(2.71828)
        writer.write_int64(-9876543210)

    with BinaryReader("file.bin") as reader:
        print(reader.read_float64())
        print(reader.read_int32())
        print(reader.read_byte())
        print(reader.read_bool())
        print(reader.read_float64())
        print(reader.read_int64())
