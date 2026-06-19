from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app.db.session import engine


def main() -> None:
    try:
        with engine.connect() as connection:
            database_name = connection.execute(text("SELECT DATABASE()")).scalar()
            current_user = connection.execute(text("SELECT CURRENT_USER()")).scalar()

        print("Conexao com MySQL realizada com sucesso.")
        print(f"Banco selecionado: {database_name}")
        print(f"Usuario conectado: {current_user}")
    except SQLAlchemyError as exc:
        print("Nao foi possivel conectar ao MySQL.")
        print(f"Erro: {exc}")
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
