# [Dr.Dart](http://www.doosanrobotics.com/kr/)
# [Example Gripper Data Gathering(DRL&Python code)]
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

## *Overview*
This example acquires gripper data from DRL running on Doosan robot controller, transfers the data to Python code running on window os through socket communication, and saves it as a file.


## *Usage*
This example must be executed in the following order.

1. Run DRL (sever_drl_code.drl) on the Doosan robot controller first.
2. Run client_save_code.py on Windows OS
3. After completing the DRL code execution, client_save_code.py is automatically terminated.
4. Check the txt sample file in the folder where client_save_code.py is located.

In the case of the created sample file, data is written in the order of time (min: sec: ms), state, and current.
(Please refer to sample_data_20230420_1614.txt.)