def secure_archive(file_path: str, action: str = 'read',
                   content: str = '') -> tuple[bool, str]:
    if action == 'read':
        try:
            with open(file_path, 'r') as f:
                content_file: str = f.read()
            return True, content_file
        except OSError as e:
            return False, str(e)
    elif action == 'write':
        try:
            with open(file_path, 'w') as f:
                f.write(content)
            return True, "Content successfully written to file"
        except OSError as e:
            return False, str(e)
    return False, "Error"


if __name__ == '__main__':
    sample: str = (
        '[FRAGMENT 001] Digital preservation protocols established 2087\n'
        '[FRAGMENT 002] Knowledge must survive the entropy wars\n'
        '[FRAGMENT 003] Every byte saved is a victory against oblivion\n'
    )
    # Prepare a regular file so the read demo below has something to recover.
    secure_archive("test.txt", "write", sample)

    print('=== Cyber Archives Security ===')
    print()
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))
    print()
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/shadow"))
    print()
    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive("test.txt"))
    print()
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_archive.txt", "write", sample))
