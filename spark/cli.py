import sys
from spark.engine import SparkEngine

def main():
    if len(sys.argv) < 2:
        print("Usage: spark-cli <concept_or_idea>")
        sys.exit(1)
        
    concept = " ".join(sys.argv[1:])
    print(f"[spark] Running ideation engine for: '{concept}'...\n")
    
    engine = SparkEngine()
    blueprint = engine.ideate(concept)
    print(blueprint)

if __name__ == "__main__":
    main()
