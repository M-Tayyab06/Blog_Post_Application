# 1. Use a lightweight official Python image
FROM python:3.11-slim

# 2. Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Set working directory
WORKDIR /app

# 4. Copy project files
COPY . /app/

# 5. Install Python dependencies
RUN pip install Pillow
RUN pip install -r requirements.txt

# 6. Expose port
EXPOSE 8000

# 7. Run the app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
