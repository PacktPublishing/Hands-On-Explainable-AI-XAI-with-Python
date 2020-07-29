**Software and hardware specifications**
========================================

<table>
<thead>
<tr class="header">
<th><strong>Chapter number</strong></th>
<th><strong>Software required<br />
(with version)</strong></th>
<th><strong>Hardware specifications</strong></th>
<th><strong>OS required</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2">1-12</td>
<td>Python 3.8</td>
<td rowspan="2">x86/AMD64 system</td>
<td rowspan="2">Windows,<br />
any Linux distro,<br />
or macOS</td>
</tr>
<tr>
<td>Any modern web browser, <br />such as Firefox, Edge, Safari, <br />or Chrome</td>
</tr>
</tbody>
</table>

**\*Note**: The code in this book is in the form of Jupyter notebooks,
and can be executed in Google Colaboratory. If you wish to execute these
on your local machine, the (Python) package requirements are mentioned
in the following section. Do keep in mind however, that these notebooks
make extensive use of Colab forms, which won't be visible when executed
on your local machine.

**Package specifications**
==========================

| **Package required** | **Version**       | **Installation command (pip)** |
|----------------------|-------------------|--------------------------------|
| Jupyter              | 1.0.0 or higher   | `pip install jupyter`          |
| TensorFlow           | 2.2.0 or higher   | `pip install tensorflow`       |
| NumPy                | 1.19.1 or higher  | `pip install numpy`            |
| SciPy                | 1.5.2 or higher   | `pip install scipy`            |
| pandas               | 1.1.0 or higher   | `pip install pandas`           |
| Matplotlib           | 3.3.0 or higher   | `pip install matplotlib`       |
| scikit-learn         | 0.23.1 or higher  | `pip install scikit-learn`     |
| shap                 | 0.35.0 or higher  | `pip install shap`             |
| lime                 | 0.2.0.1 or higher | `pip install lime`             |
| facets-overview      | 1.0.0 or higher   | `pip install facets-overview`  |
| witwidget            | 1.7.0 or higher   | `pip install witwidget`        |

**\*Note**: This isn't an exhaustive list of all the packages required
to run the codes in this book, but only the essential and most commonly
used packages in the book. You will likely encounter some more required
packages as you read through the book, which you can install using `pip`
or `conda`.

**Additional requirement**
==========================

*Chapter 7*, *A Python Client for Explainable AI Chatbots*, requires a
Google Cloud Platform account. For pricing details, visit:
<https://cloud.google.com/pricing>.
