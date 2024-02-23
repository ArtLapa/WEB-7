# alembic/env.py
from sqlalchemy import engine_from_config, create_engine
from sqlalchemy import pool
from alembic import context
from models import Base
import os
import sys

# Додаємо шлях до sys.path для правильного імпорту моделей
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Імпортуємо моделі
from models import Student, Group, Teacher, Subject, Grade

# Підключаємося до бази даних
config = context.config
config.set_main_option('sqlalchemy.url', 'postgresql://your_username:your_password@localhost:5432/your_database_name')
target_engine = create_engine(config.get_main_option('sqlalchemy.url'))

# Здійснюємо міграції для всіх моделей
with target_engine.connect() as connection:
    context.configure(
        connection=connection,
        target_metadata=Base.metadata,
        compare_type=True,
        compare_server_default=True,
    )

    with context.begin_transaction():
        context.run_migrations()

