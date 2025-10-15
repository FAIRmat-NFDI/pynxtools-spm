From jupyter/scipy-notebook:2023-03-20

# Define environment variable
ENV HOME=/home/jovyan
WORKDIR $HOME

# To copy requirements.txt file in container
ADD requirements.txt .
COPY example/ ./work_dir/example

# Intallation of other jupyter extension in jupyter/scipy-notebook
RUN pip install -r requirements.txt \
    && jupyter lab build \
    && jupyter nbextension enable --py widgetsnbextension \
    && jupyter serverextension enable jupyterlab_h5web

# After instalation removing the requirement file
RUN rm requirements.txt
