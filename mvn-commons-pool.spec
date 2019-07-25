#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-commons-pool
Version  : 1.5.4
Release  : 3
URL      : https://repo1.maven.org/maven2/commons-pool/commons-pool/1.5.4/commons-pool-1.5.4.jar
Source0  : https://repo1.maven.org/maven2/commons-pool/commons-pool/1.5.4/commons-pool-1.5.4.jar
Source1  : https://repo1.maven.org/maven2/commons-pool/commons-pool/1.5.4/commons-pool-1.5.4.pom
Source2  : https://repo1.maven.org/maven2/commons-pool/commons-pool/1.6/commons-pool-1.6.jar
Source3  : https://repo1.maven.org/maven2/commons-pool/commons-pool/1.6/commons-pool-1.6.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-commons-pool-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-commons-pool package.
Group: Data

%description data
data components for the mvn-commons-pool package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-pool/commons-pool/1.5.4
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/commons-pool/commons-pool/1.5.4/commons-pool-1.5.4.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-pool/commons-pool/1.5.4
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/commons-pool/commons-pool/1.5.4/commons-pool-1.5.4.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-pool/commons-pool/1.6
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/commons-pool/commons-pool/1.6/commons-pool-1.6.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-pool/commons-pool/1.6
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/commons-pool/commons-pool/1.6/commons-pool-1.6.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/commons-pool/commons-pool/1.5.4/commons-pool-1.5.4.jar
/usr/share/java/.m2/repository/commons-pool/commons-pool/1.5.4/commons-pool-1.5.4.pom
/usr/share/java/.m2/repository/commons-pool/commons-pool/1.6/commons-pool-1.6.jar
/usr/share/java/.m2/repository/commons-pool/commons-pool/1.6/commons-pool-1.6.pom
