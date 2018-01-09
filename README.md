# Site block

Basic idea behind this small project was to start `tshark` and listen to http traffic. If there is some nasty word in traffic which are saved in `nasty_wrds.txt`, whole communication from PC will be blocked for time in `delay.txt`. 

Problems & dependencies:
 * Place & rename whole repository into `/usr/share/contBlock/`
    * That is cause I had to do some `.deb` package and repository respects that 
 * Tested only under Ubuntu Linux
 * Use `tshark` it should be installed with `wireshark` package

