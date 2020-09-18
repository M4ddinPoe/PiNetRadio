import {Radio} from "../../models/Radio";
import {Inject, Injectable} from "@angular/core";
import {LOCAL_STORAGE, StorageService} from "ngx-webstorage-service";

@Injectable({
  providedIn: 'root',
})
export class LocalStorageRepository {

  constructor(@Inject(LOCAL_STORAGE) private storage: StorageService) { }

  public setLastRadio(radio: Radio): void {
    this.storage.set('lastRadio', radio);
  }

  public getLastRadio(): Radio {
    return this.storage.get('lastRadio');
  }

  public setLastVolume(volume: number): void {
    this.storage.set('lastVolume', volume);
  }

  public getLastVolume(): number {
    return this.storage.get('lastVolume');
  }
}
