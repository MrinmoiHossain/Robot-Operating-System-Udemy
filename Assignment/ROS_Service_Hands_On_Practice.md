### 1. Open the Turtlesim simulator
```bash
$ rosrun turtlesim turtlesim_node
```
### 2. Display the list of services
```bash
$ rosservice list
```
### 3. What is the command that shows the information of the service /reset
```bash
$ rosservice info /reset
```
### 4. Write the result of the execution of the command for the service /reset
```
Node: /turtlesim
URI: rosrpc://mrinmoi-HP-Pavilion-Notebook:44865
Type: std_srvs/Empty
Args:
```
### 5. What is the command that shows the information of the service /kill
```bash
$ rosservice info /kill
```
### 6. Write the result of the execution of the command for the service /kill
```
Node: /turtlesim
URI: rosrpc://mrinmoi-HP-Pavilion-Notebook:44865
Type: turtlesim/Kill
Args: name

```
### 7. What is the command that shows the content of message turtlesim/Kill of the /kill service?
```bash
$ rossrv info turtlesim/Kill
```
### 8. Spaw one additional turtle called tsim1. Write the command. Spaw one additional turtle called tsim1. Write the command.
```bash
$ rosservice call /spawn 3 3 0 tsim1
$ rosservice call /spawn 7 7 0 tsim2
```
### 9. use the service kill to kill tsim1.Write the command. 
```bash
$ rosservice call /kill tsim1
```
### 10. use the service reset to reset all the simulation. Write the command. 
```bash
$ rosservice call /reset
```
