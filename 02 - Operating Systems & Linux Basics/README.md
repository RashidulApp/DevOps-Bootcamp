## Operating Systems & Linux Basics

Title: Exploring Operating Systems: Functions, Components, and the Virtualization Advantage

Introduction to Operating Systems:

Operating systems (OS) are the unsung heroes of computing, providing a crucial layer of abstraction between hardware and user applications. In this overview, we delve into the pivotal tasks performed by operating systems, ranging from process and memory management to storage, security, networking, and the indispensable kernel.

Tasks of an Operating System:

1. **Process Management:**
   - A process is a small unit executing on a computer, with its own isolated space.
   - Efficient memory allocation is essential as RAM is limited.
   - Memory swapping occurs when RAM is exhausted, impacting computer speed.

2. **Memory Management:**
   - Allocating working memory for each application.
   - Addressing the limitation of RAM through memory swapping.
  
3. **Storage Management:**
   - Involves secondary memory (hard drive) for persistent data storage.
   - Managing the file system in a structured manner.

4. **Management of I/O Devices:**
   - Ensures seamless interaction with input/output devices.

5. **Security:**
   - Manages users and permissions, providing each user with its own space and specific permissions.

6. **Networking:**
   - Involves tasks such as port management and IP addressing.

Operating Systems Components:

- **Kernel:**
   - The heart or brain of the operating system.
   - Serves as the intermediary between software and hardware.

- **Standards:**
   - POSIX (Portable Operating Systems) ensures compatibility across diverse systems.

- **Virtualization:**
   - Eliminates the need for separate hardware, facilitating efficient resource utilization.

- **Hypervisor:**
   - Examples include VirtualBox, acting as an intermediary to create virtual machines.
   - Differentiates between Type 1 (bare metal) and Type 2 (installed on top of an OS) hypervisors.

   - **Benefits of Virtualization:**
      - Learn and experiment without jeopardizing the main OS.
      - Test applications on different OS environments.

   - **Why Companies Adopt Virtualization:**
      - Abstraction of the OS from hardware, creating portable virtual machine images.

Installation and Basic Configuration of Virtualbox:

- **Basic Installation:**
   - Follow the straightforward installation process.

- **Useful Tweaks:**
   - Share clipboard between host and guest machines:
      - Virtualbox menu -> Machine -> Settings -> Advanced -> Shared Clipboard.
   - Enhance functionality with the Virtualbox extension pack: [Virtualbox Extension Pack](https://www.virtualbox.org/wiki/Downloads).



### Linux File System

In the Linux realm, everything is a file, distinguishing it from macOS and Windows. The root user has a dedicated home directory, with variations across different operating systems (e.g., `/Users/username` in macOS).

#### Linux Folder Structure

- **/home/{Username}:** Directory for non-root users with assigned home directories.
- **/bin:** Executables for essential system commands.
- **/sbin:** System binaries requiring superuser privileges.
- **/lib:** Shared libraries for executions from /bin or /sbin.
- **/usr:** Historical user home directory, with /usr/local housing user-installed programs.
- **/opt:** Repository for third-party programs without component separation.
- **/boot:** Files essential for booting.
- **/etc:** System configuration files.
- **/dev:** Device files (e.g., webcam, mouse, keyboard).
- **/var:** Stores logs, cache, temporary resources, and more.
- **/media:** Reserved for removable media.
- **/mnt:** Temporary mount points.

*Hidden files (starting with a dot)*

### Commands

A comprehensive set of commands for efficient navigation and manipulation in the Linux terminal:

- **pwd:** Show the current directory.
- **ls:** List contents.
- **cd:** Change directory.
- **mkdir:** Make directory.
- **touch:** Create file.
- **rm:** Delete file.
- **clear:** Clear the terminal.
- **mv:** Rename or move files.
- **cp -r:** Copy contents from one folder to another.
- **ls -R:** List all folders and files recursively.
- **history:** Display recent commands.
- **ls -a:** Display hidden files.
- **ls -l:** Print files in a long list format.
- **cat:** Show contents of a file.
- **uname -a:** Show system and kernel information.
- **cat /etc/os-release:** Display release version.
- **lscpu:** Show CPU information.
- **lsmem:** Show memory information.
- **sudo:** Grant superuser privileges.
- **su - \<username>:** Switch to a different user.
- **|:** Pipe, pass output from one command as input to the next.
- **\<input> | less:** Display reader-friendly format in the CLI.
- **\<input> | grep \<pattern>:** Filter input based on pattern search.
- **\>:** Redirect, send output to a file.
- **\>\>:** Append text to the end of a file.
- **\>\> Can pass multiple commands in one line, separated by ;**

### Package Manager: APT

APT (Advanced Package Tool) simplifies software management by resolving dependencies, ensuring package integrity, and facilitating downloads, installations, and updates. Key commands include:

```bash
apt search <package name>
apt install <package name>
apt remove <package name>
apt update
apt upgrade
apt autoremove
apt full-upgrade
```

### VIM Text Editor

Mastering the VIM text editor is essential for efficient text manipulation:

- **:wq:** Quit and save.
- **:q!:** Quit without saving.
- **dd:** Delete a line.
- **d10d:** Delete the next 10 lines.
- **u:** Undo.
- **A:** Jump to the end of a line and switch to insert mode.
- **$:** Jump to the end of a line without switching to insert mode.
- **0:** Jump to the beginning of a line.
- **12G:** Jump to line 12.
- **/pattern:** Search for a pattern.
- **n:** Jump to the next match.
- **N:** Jump to the previous match.
- **:%s/old/new:** Replace old with new throughout the file.

### Users, Groups & Permissions

Understanding user management and permissions is crucial for system security:

#### Commands

- **adduser \<username>:** Add a new user.
- **passwd \<username>:** Set a password for a user.
- **su - \<username>:** Switch to a different user.
- **su -:** Switch to the root user.
- **groupadd \<groupname>:** Create a new group.
- **deluser \<username>:** Delete a user.
- **groupdel \<groupname>:** Delete a group.
- **usermod [OPTIONS] \<username>:** Modify user attributes.
- **usermod -g \<groupname> \<username>:** Change the primary group of a user.
- **usermod -G \<groupname> \<username>:** Override the secondary groups list.
- **usermod -aG \<groupname> \<username>:** Append to the existing list of secondary groups.
- **gpasswd -d \<username> \<groupname>:** Remove a user from a group.
- **groups \<username>:** List the groups a user belongs to.
- **exit:** Logout a user.
- **chown \<username>:\<groupname> \<filename>:** Change file ownership.
- **chgrp \<groupname> \<filename>:** Change group ownership.

#### Permissions

**(Owner)**
- **r:** Read
- **w:** Write
- **x:** Execute
- **-:** No permission

**(Group)**
- **r:** Read
- **w:** Write
- **x:** Execute
- **-:** No permission

**(Other)**
- **r:** Read
- **w:** Write
- **x:** Execute
- **-:** No permission

##### Chmod

Useful chmod commands for managing permissions:

- **chmod -x \<filename>:** Remove execute permissions for all owners.
- **chmod g-w \<filename>:** Remove write permissions for the group.
- **chmod g+x \<filename>:** Add execute permissions for the group.
- **chmod u+x \<filename>:** Add execute permission for the user.
- **chmod o+x \<filename>:** Add execute permission for others.
- **chmod g=rwx \<filename>:** Set specific block permissions for the group.
- **chmod 777 \<filename>:** Give all permissions to all owners.