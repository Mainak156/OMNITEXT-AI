from core.task_classifier import classify_task
from core.router import route_tasks
from core.aggregator import aggregate_results

class Orchestrator:
    def __init__(self):
        pass

    def run(self, user_input, context=None):
        print("\n[1] Classifying tasks...")
        tasks = classify_task(user_input)

        if not tasks:
            print("[!] No task detected → defaulting to generation")
            tasks = ["generation"]

        print("[2] Routing tasks...")
        results = route_tasks(tasks, user_input, context)

        print("[3] Aggregating results...")
        final_output = aggregate_results(results, tasks, user_input)

        return final_output