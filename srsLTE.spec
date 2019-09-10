Name:           srsLTE
Version:        %{VERSION}
Release:        %{RELEASE}%{?dist}
Summary:        Open source SDR LTE software suite from Software Radio Systems (SRS) 
Group:          System Environment/Libraries
License:	GNU
URL:            https://github.com/srsLTE/srsLTE
Source:         %{name}-%{version}.tar.gz      
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  cmake
BuildRequires:  fftw3-devel
BuildRequires:  lksctp-tools-devel
BuildRequires:  libconfig-devel
BuildRequires:  boost-devel

%description
Open source SDR LTE software suite from Software Radio Systems (SRS) 

%package devel
Summary:	%{name} development package
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Development files for %{name}.

%prep
%setup -n srsLTE-release_19_06

%build
mkdir build
pushd build
%cmake -DENABLE_SRSUE=OFF ..
make %{?_smp_mflags}
popd

%check
pushd build
make test

%install
pushd build
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
ldconfig

%postun
ldconfig

%files
%defattr(-,root,root,-)
%doc LICENSE README.md
%{_bindir}/*
%{_libdir}/*.so
%{_datadir}/srslte/

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.a
%{_includedir}/srslte

%changelog
