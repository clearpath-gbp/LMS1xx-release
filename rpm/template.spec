Name:           ros-kinetic-lms1xx
Version:        0.1.5
Release:        0%{?dist}
Summary:        ROS lms1xx package

Group:          Development/Libraries
License:        LGPL
URL:            http://ros.org/wiki/LMS1xx
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-rosconsole-bridge
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-roscpp-serialization
Requires:       ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-rosconsole-bridge
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-roscpp-serialization
BuildRequires:  ros-kinetic-roslaunch
BuildRequires:  ros-kinetic-roslint
BuildRequires:  ros-kinetic-rosunit
BuildRequires:  ros-kinetic-sensor-msgs

%description
The lms1xx package contains a basic ROS driver for the SICK LMS1xx line of
LIDARs.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Thu May 05 2016 Mike Purvis <mpurvis@clearpathrobotics.com> - 0.1.5-0
- Autogenerated by Bloom

