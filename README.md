
# Please do not delete!

This repo is not a shippable ManiVault Studio plugin. 

It's exists purely to test parts of the ci system used ManiVault.

## CI Tester

This branch is testing conan v2 and the new lkebartifactory.nl Artifactory.

### Testing multi build_type build

This repo consumes single package dependencies from conancenter and demonstrates
an approach to multi build_type building in the ci. Muti build_type building
is triggered by supplying a build type conprising a comma separate set of
build types e.g. "Release, RelWithDebInfo" . Not that the build types must be from the supported list:

- Debug
- Release
- RelWithDebInfo
- MinSizeRel

To support this a layout() method must be supplied with a self.folders.build and the package() method
should support being called multiple times .

### Dependencies

The fmt library is used as an example dependency - it also pulls in lz4.
