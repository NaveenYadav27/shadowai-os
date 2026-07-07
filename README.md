# ShadowAI OS - Enterprise AI Operating System

🚀 **Enterprise-grade AI Agent Orchestration Platform** with local-first architecture, multi-agent workflows, and intelligent task automation.

## 🎯 Features

### 🤖 Multi-Agent Orchestration
- Deploy and manage multiple AI agents with different capabilities
- Intelligent agent selection and load balancing
- Dependency management and task sequencing
- Real-time execution monitoring

### 🔄 Workflow Automation
- Visual workflow builder
- Complex state machines and branching logic
- Error handling and retry policies
- Async and parallel task execution

### 🧠 AI-First Design
- **Local First**: Ollama integration for on-premises LLMs
- Multiple AI providers: OpenRouter, Groq, HuggingFace
- Model fine-tuning and prompt optimization
- Knowledge base integration
- Specialized agents for different domains

### 📊 Enterprise Features
- Multi-project support
- Role-based access control (RBAC)
- Comprehensive audit logging
- Performance analytics and cost tracking
- Data encryption and compliance ready

### 🔌 Extensible Architecture
- Plugin system for custom agents
- REST API for third-party integrations
- WebSocket support for real-time updates
- Event-driven architecture

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────┐
│          Frontend (React + TypeScript)              │
│     Dashboard | Workflow Builder | Monitoring       │
└──────────────┬──────────────────────────────────────┘
               │
┌──────────────▼──────────────────────────────────────┐
│         API Gateway (FastAPI)                       │
│    Authentication | Routing | Rate Limiting        │
└──────────────┬──────────────────────────────────────┘
               │
┌──────────────▼──────────────────────────────────────┐
│       Core Services (Microservices)                 │
├─────────────────────────────────────────────────────┤
│  • Agent Manager    • Workflow Engine               │
│  • Task Scheduler   • Knowledge Service             │
│  • Artifact Store   • Prompt Manager                │
└──────────────┬──────────────────────────────────────┘
               │
┌──────────────▼──────────────────────────────────────┐
│    Data Layer & Message Queue                       │
├─────────────────────────────────────────────────────┤
│  PostgreSQL │ Redis │ Elasticsearch │ MinIO        │
└─────────────────────────────────────────────────────┘
               │
┌──────────────▼──────────────────────────────────────┐
│    AI/LLM Layer                                      │
├─────────────────────────────────────────────────────┤
│  Ollama (Local) │ OpenRouter │ Groq │ HuggingFace   │
└─────────────────────────────────────────────────────┘
```

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose
- Python 3.11+ (for local development)
- Node.js 18+ (for frontend)
- 4GB+ RAM, 20GB disk space

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/NaveenYadav27/shadowai-os.git
cd shadowai-os
```

2. **Set up environment**
```bash
cp .env.example .env
# Edit .env with your configuration
```

3. **Start with Docker Compose**
```bash
docker-compose up -d
```

4. **Initialize database**
```bash
docker-compose exec backend alembic upgrade head
```

5. **Access the application**
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

### Local Development

**Backend**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

**Frontend**
```bash
cd frontend
npm install
npm run dev
```

## 📖 Configuration

### Environment Variables

```env
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/shadowai_db

# Redis
REDIS_URL=redis://localhost:6379/0

# AI Providers
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_ENABLED=true

OPENROUTER_API_KEY=your_key_here
GROQ_API_KEY=your_key_here

# Default Models
DEFAULT_FRONTEND_MODEL=deepseek-coder
DEFAULT_BACKEND_MODEL=deepseek
DEFAULT_REASONING_MODEL=deepseek-r1
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with FastAPI, React, and PostgreSQL
- AI powered by Ollama and various LLM providers
- Inspired by enterprise AI orchestration platforms

## 📧 Support

- GitHub Issues: [Report bugs](https://github.com/NaveenYadav27/shadowai-os/issues)
- Discussions: [Ask questions](https://github.com/NaveenYadav27/shadowai-os/discussions)
- Email: support@shadowai.dev

---

**Made with ❤️ for the AI-powered future**
