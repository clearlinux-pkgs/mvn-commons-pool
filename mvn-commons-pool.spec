#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-commons-pool
Version  : 1.5.4
Release  : 5
URL      : https://repo1.maven.org/maven2/commons-pool/commons-pool/1.5.4/commons-pool-1.5.4.jar
Source0  : https://repo1.maven.org/maven2/commons-pool/commons-pool/1.5.4/commons-pool-1.5.4.jar
Source1  : https://repo.maven.apache.org/maven2/org/apache/commons/commons-pool2/2.5.0/commons-pool2-2.5.0.jar
Source2  : https://repo.maven.apache.org/maven2/org/apache/commons/commons-pool2/2.5.0/commons-pool2-2.5.0.pom
Source3  : https://repo1.maven.org/maven2/commons-pool/commons-pool/1.5.4/commons-pool-1.5.4.pom
Source4  : https://repo1.maven.org/maven2/commons-pool/commons-pool/1.6/commons-pool-1.6.jar
Source5  : https://repo1.maven.org/maven2/commons-pool/commons-pool/1.6/commons-pool-1.6.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-commons-pool-data = %{version}-%{release}
Requires: mvn-commons-pool-license = %{version}-%{release}
BuildRequires : apache-maven
BuildRequires : buildreq-mvn

%description
No detailed description available

%package data
Summary: data components for the mvn-commons-pool package.
Group: Data

%description data
data components for the mvn-commons-pool package.


%package license
Summary: license components for the mvn-commons-pool package.
Group: Default

%description license
license components for the mvn-commons-pool package.


%prep
%setup -q -n META-INF

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-commons-pool
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-commons-pool/LICENSE.txt
mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-pool/commons-pool/1.5.4
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/commons-pool/commons-pool/1.5.4/commons-pool-1.5.4.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-pool2/2.5.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-pool2/2.5.0/commons-pool2-2.5.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-pool2/2.5.0
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-pool2/2.5.0/commons-pool2-2.5.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-pool/commons-pool/1.5.4
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/commons-pool/commons-pool/1.5.4/commons-pool-1.5.4.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-pool/commons-pool/1.6
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/commons-pool/commons-pool/1.6/commons-pool-1.6.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-pool/commons-pool/1.6
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/commons-pool/commons-pool/1.6/commons-pool-1.6.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/commons-pool/commons-pool/1.5.4/commons-pool-1.5.4.jar
/usr/share/java/.m2/repository/commons-pool/commons-pool/1.5.4/commons-pool-1.5.4.pom
/usr/share/java/.m2/repository/commons-pool/commons-pool/1.6/commons-pool-1.6.jar
/usr/share/java/.m2/repository/commons-pool/commons-pool/1.6/commons-pool-1.6.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-pool2/2.5.0/commons-pool2-2.5.0.jar
/usr/share/java/.m2/repository/org/apache/commons/commons-pool2/2.5.0/commons-pool2-2.5.0.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-commons-pool/LICENSE.txt
