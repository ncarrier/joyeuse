# how to create a release

1. set version in joyeuse/__version__.py and in all .po files
2. add a changelog entry in debian/changelog
3. verify the manuals
4. create a fake release by pushing a test tag
5. download the artifacts
6. test them:
   * test the exe with wine
   * test the .debs with docker
   * test the pip archive in a venv
