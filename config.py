param_rf = {'n_estimators': list(range(10,101,10)),
              'criterion': ['entropy'],
              'max_depth': list(range(5,11,1)),
              'min_samples_split': [20]}

param_log = {"solver":["liblinear"],
             "penalty":["l2","l1"],
             "max_iter":[80,90,100],
             "C":[0.9,1,1.1,1.2,1.3]}

param_gb = {'loss': ['deviance','exponential'],
              'n_estimators': list(range(60,101,10)),
              'subsample': [0.6,0.7,0.8,1],
              'max_depth': list(range(3,8,1))}

param_xgb = {'max_depth': [5,10,15],
              'learning_rate': [0.001,0.003],
              'n_estimators': [10,50,100]}