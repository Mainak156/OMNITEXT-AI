from core.orchestrator import Orchestrator

if __name__ == "__main__":
    orchestrator = Orchestrator()

    user_input = input("Enter your request: ")

    result = orchestrator.run(user_input)

    print(result)