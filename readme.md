## Installation

1. **Install Docker and Docker Compose**  
This project uses Docker to containerize the app, please make sure Docker is installed.

2. **Clone the repo**

```bash
git clone https://github.com/Karasu-huginn/Hiboutik_LittleBill.git
cd Hiboutik_LittleBill
```

3. **Build and start the container**

```bash
docker compose up --build
```

Will then start:
- **FastAPI backend** at [http://localhost:8000](http://localhost:8000)
- **React frontend (dev mode)** at [http://localhost:5173](http://localhost:5173)  
- **PostgreSQL database** at db:5432
