"""
Basic usage example for the spark engine.
"""

from spark.engine import SparkEngine

def run_example():
    concept = "AI Agent Task Automation Pipeline"
    print(f"Running spark engine for: '{concept}'...\n")

    engine = SparkEngine()
    blueprint = engine.ideate(concept)
    
    print("=" * 60)
    print(blueprint)
    print("=" * 60)

if __name__ == "__main__":
    run_example()
