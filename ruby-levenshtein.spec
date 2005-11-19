Summary:	Module to calculate Levenshtein distance
Summary(pl):	Modu³ do obliczania odleg³o¶ci Levenshteina
Name:		ruby-levenshtein
Version:	0.1
Release:	1
License:	GPL
Group:		Development/Libraries
Source0:	http://po-ru.com/files/levenshtein.rb
# Source0-md5:	78b3632772c3baa4c00e8704339ecd04
BuildRequires:	rpmbuild(macros) >= 1.263
Source1:	setup.rb
URL:		http://po-ru.com/files/levenshtein.rb
BuildRequires:	ruby
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Module to calculate Levenshtein distance.

%description -l pl
Modu³ do obliczania odleg³o¶ci Levenshteina.

%prep
%setup -qcT
mkdir lib
cp %{SOURCE0} lib
cp %{SOURCE1} .

%build
ruby setup.rb config \
	--siterubyver=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup
rdoc --inline-source --op rdoc lib
rdoc --ri --op ri lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_rubylibdir}/*
%{ruby_ridir}/Levenshtein
