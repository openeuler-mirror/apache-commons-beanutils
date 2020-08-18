%global base_name    beanutils
%global short_name   commons-%{base_name}
Name:                apache-%{short_name}
Version:             1.9.4
Release:             1
Summary:             Java utility methods for accessing and modifying the properties of arbitrary JavaBeans
License:             ASL 2.0
BuildArch:           noarch
URL:                 http://commons.apache.org/%{base_name}
Source0:             http://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
BuildRequires:       maven-local mvn(commons-collections:commons-collections)
BuildRequires:       mvn(commons-collections:commons-collections-testframework)
BuildRequires:       mvn(commons-logging:commons-logging) mvn(junit:junit)
BuildRequires:       mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:       mvn(org.apache.maven.plugins:maven-antrun-plugin)
%description
The scope of this package is to create a package of Java utility methods
for accessing and modifying the properties of arbitrary JavaBeans.  No
dependencies outside of the JDK are required, so the use of this package
is very lightweight.

%package javadoc
Summary:             Javadoc for %{name}
%description javadoc
%{summary}.

%prep
%setup -q -n %{short_name}-%{version}-src
sed -i 's/\r//' *.txt
%pom_remove_plugin :maven-assembly-plugin
%mvn_alias :{*} :@1-core :@1-bean-collections
%mvn_alias :{*} org.apache.commons:@1 org.apache.commons:@1-core org.apache.commons:@1-bean-collections
%mvn_file : %{name} %{name}-core %{name}-bean-collections
%mvn_file : %{short_name} %{short_name}-core %{short_name}-bean-collections

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc RELEASE-NOTES.txt
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Wed Jul 29 2020 yaokai <yaokai13@huawei.com> - 1.9.4-1
- package init
