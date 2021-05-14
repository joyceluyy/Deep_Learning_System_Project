This git repository contains the code for the Deep Learning System Sp21 final project.
** Seinfeld TV Scripts Generator**
We would like to design and train deep neural networks that generate TV scripts for the show Seinfeld.

It should be able to 1.generate TV script for each character. 2. generate dialogue between two characters that frequently chat with each other.

***Team members***
Joyce Lu (yl6211), Miaozhi Yu (my1251)

*** Running Locally ***
Create a virtual environment:
```virtualenv ~/.virtualenvs/script_generator```

Activate the virtual environment:
```. ~/.virtualenvs/script_generator/bin/activate```

Install required packages:
```pip install -r ./nmt/requirements```

For LSTM and GRU, please make sure that you use keras framework.

- Run ```./nmy/run/sh -vocab``` to create source sentences and target sentences for the NMT model.

For NMT, please make sure that you use Pytorch >= 1.0.0.
- Run ```./nmt/run.sh -train``` for training.

- Run ```./nmt/run.sh -test``` for testing.

*** Reference ***
For NMT model, we modified the code used in this github: https://github.com/samjkwong/NLG-NMT/tree/master/nmt

For GRU model, we consulted this source https://www.geeksforgeeks.org/ml-text-generation-using-gated-recurrent-unit-networks/

For bidirectional LSTM model, we consulted this source https://medium.com/@david.campion/text-generation-using-bidirectional-lstm-and-doc2vec-models-2-3-f0fc07ee7b30


