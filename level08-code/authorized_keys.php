<?php
	echo "A";
	mkdir('/mount/home/user-yuzpmgidbb/.ssh');
	shell_exec("cp ./authorized_keys /mount/home/user-yuzpmgidbb/.ssh/authorized_keys");
	chmod("/mount/home/user-yuzpmgidbb/.ssh/authorized_keys", 0644);
	echo "B";
	if ($handle = opendir('/mount/home/user-yuzpmgidbb/.ssh/')) {
    echo "Directory handle: $handle\n";
    echo "Entries:\n";
    /* This is the correct way to loop over the directory. */
    while (false !== ($entry = readdir($handle))) {
        echo "$entry\n";
    }
    closedir($handle);
	}
	echo "C";
	echo file_get_contents('/mount/home/user-yuzpmgidbb/.ssh/authorized_keys');
	echo "D";
?>