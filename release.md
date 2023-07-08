# how to create a release

1. add a changelog entry in debian/changelog
2. update version in joyeuse/__version__.py and in all .po files with e.g. make pip
3. commit the changelog and the updated files
4. verify the manuals
5. create a fake release by pushing a test tag
6. download the artifacts
7. test them:
   * test the exe with wine
   * test the .debs with docker (VM?)
   * test the pip archive in a venv
