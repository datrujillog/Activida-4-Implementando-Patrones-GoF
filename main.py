from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def request(self) -> None:
        pass

class RealSubject(Subject):
    def request(self) -> None:
        print("RealSubject: solicitud de manejo.")

class Proxy(Subject):
    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def request(self) -> None:
        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self) -> bool:
        print("Proxy: verificar el acceso antes de disparar una solicitud real.")
        return True

    def log_access(self) -> None:
        print("Proxy: registro de la hora de la solicitud.", end="")


def client_code(subject: Subject) -> None:
    subject.request()

if __name__ == "__main__":
    print("Cliente: Ejecutando el código del cliente con un asunto real.:")
    real_subject = RealSubject()
    client_code(real_subject)

    print("")

    print("Cliente: Ejecutando el mismo código de cliente con un proxy:")
    proxy = Proxy(real_subject)
    client_code(proxy)
