import matplotlib.pyplot as plt
import numpy as np

def generate_heatmap(results_data):
    """
    Generates comparison heatmap for all models and metrics
    """
    models = ['DistilGPT2', 'TinyLlama', 'Phi-2']
    metrics = ['Accuracy', 'Consistency', 'Reliability', 'Hallucination Rate']
    
    # Results data ila undali (example)
    data = np.array([
        [3.0,  45.0, 25.0, 85.0],   # DistilGPT2
        [15.0, 65.0, 55.0, 60.0],   # TinyLlama
        [42.0, 80.0, 75.0, 35.0],   # Phi-2
    ])
    
    fig, ax = plt.subplots(figsize=(10, 6))
    im = ax.imshow(data, cmap='RdYlGn')
    
    ax.set_xticks(np.arange(len(metrics)))
    ax.set_yticks(np.arange(len(models)))
    ax.set_xticklabels(metrics)
    ax.set_yticklabels(models)
    
    # Numbers show cheyyi inside cells
    for i in range(len(models)):
        for j in range(len(metrics)):
            ax.text(j, i, f'{data[i, j]}%',
                   ha="center", va="center",
                   color="black", fontsize=12)
    
    ax.set_title("Model Performance Heatmap — All Metrics", 
                 fontsize=14, fontweight='bold')
    plt.colorbar(im)
    plt.tight_layout()
    plt.savefig('results/report/hallucination_heatmap.png', dpi=150)
    plt.show()
    print("Heatmap saved!")