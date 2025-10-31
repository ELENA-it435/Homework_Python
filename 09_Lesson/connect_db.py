from sqlalchemy import create_engine, text

engine = create_engine(
    "postgresql://postgres:Kolosokelena1%29@localhost:5432/postgres"
)

with engine.connect() as connection:
    result = connection.execute(text("SELECT version();"))
    print(result.fetchone()[0])

engine.dispose()
