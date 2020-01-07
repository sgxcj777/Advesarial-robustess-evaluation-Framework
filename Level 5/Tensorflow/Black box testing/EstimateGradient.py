import numpy as np

class EstimateGradient:
    def __init__(self,model,model_s,x,y,sigma,q):
        self.model = model
        self.model_s = model_s
        self.x = x
        self.y = y
        self.sigma = sigma
        self.q = q
        self.D = len(x.shape)
        
    def get_v(model_s,x,y):
        return model_s.get_grad(x,y)
    
    def cosSimilarity(x,y,sigma,v,s):
        numer = (model.predict(x+sigma*v) - model.predict(x))/sigma
        denom = 0
        w = ()
        s = np.random.uniform(x.shape[0])
        for i in range(1,q+1):
            
            denom +=
            
        
        
        
    